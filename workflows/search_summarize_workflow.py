# workflows/search_summarize_workflow.py
from workflows.workflow_base import WorkflowBase
from schemas.task_input import TaskInput
from schemas.task_result import TaskResult
from model_client import ask_deepseek
from function_manager import FunctionManager

class SearchSummarizeWorkflow(WorkflowBase):
    async def run(self, task: TaskInput) -> TaskResult:
        print(f"🚀 开始搜索总结任务: {task.task}")

        # Step 1: 搜索阶段
        search_result = await FunctionManager.execute_function("SearchWebTool", {"query": task.task})
        print("\n🔍 [搜索结果内容] 前500字：\n", search_result[:500])

        links = self.extract_links(search_result)
        print(f"\n🔗 [提取到的有效链接数量]: {len(links)}")
        for idx, link in enumerate(links, 1):
            print(f"  {idx}. {link}")

        if not links:
            return TaskResult(
                content="未能找到相关链接。",
                used_tools=["SearchWebTool"],
                logs_path=""
            )

        all_summaries = []
        used_tools = ["SearchWebTool", "FetchWebContentTool"]

        # Step 2: 抓取和局部总结阶段
        for idx, link in enumerate(links, 1):
            print(f"\n🌐 开始抓取第 {idx} 个链接内容: {link}")

            # 抓取正文
            content = await FunctionManager.execute_function("FetchWebContentTool", {"url": link})
            if not content or "失败" in content:
                print(f"⚠️ 抓取失败或内容无效，跳过该链接。")
                continue
            print(f"✅ 抓取成功，正文前300字：\n{content[:300]}")

            # 总结正文
            print("✍️ 开始总结网页内容...")
            summary_result = await ask_deepseek(
                f"请总结以下网页内容，控制在300字以内：\n{content[:4000]}",
                use_function_calling=False
            )
            print(f"✅ 单页总结完成，前300字：\n{summary_result.content[:300]}")

            all_summaries.append(f"🔗 {link}\n{summary_result.content}\n")

        # Step 3: 整合综合总结阶段
        if all_summaries:
            print("\n🛠 开始综合多网页总结...")
            combined_text = "\n\n".join(all_summaries)
            final_summary = await ask_deepseek(
                f"以下是多个网页内容的总结，请重新归纳成一份逻辑清晰、完整准确、控制在800字以内的大总结：\n{combined_text}",
                use_function_calling=False
            )
            final_report = final_summary.content
            print("\n📄 [最终综合总结前500字]：\n", final_report[:500])
        else:
            final_report = "未能有效总结任何网页。"
            print("\n⚠️ 最终无有效内容可总结。")

        return TaskResult(
            content=final_report,
            used_tools=used_tools,
            logs_path=""
        )

    @staticmethod
    def extract_links(search_text: str) -> list:
        import re
        pattern = r"🔗 (https?://[^\s]+)"
        return re.findall(pattern, search_text)
