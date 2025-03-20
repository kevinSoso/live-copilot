import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class FaissSearch:
    def __init__(self, model_name="all-MiniLM-L6-v2", index_file="faq_index.faiss"):
        """
        初始化 Faiss，加载 Sentence-Transformers 模型
        """
        self.model = SentenceTransformer(model_name)  # 加载文本嵌入模型
        self.d = 384  # all-MiniLM-L6-v2 的向量维度是 384
        self.index_file = index_file
        
        try:
            self.index = faiss.read_index(index_file)  # 读取已有索引
            print(f"🔹 成功加载已有 Faiss 索引: {index_file}")
        except:
            self.index = faiss.IndexFlatL2(self.d)  # L2 距离索引
            print(f"⚠️ 未找到索引文件，创建新索引: {index_file}")

        self.questions = []  # 存储问题文本
        self.answers = []  # 存储对应答案


    def add_data(self, question, answer):
        """
        添加单个问题-答案对，并更新索引
        """
        vector = np.array([self.model.encode(question)], dtype="float32")  # 编码问题
        self.index.add(vector)  # 添加到 Faiss
        self.questions.append(question)
        self.answers.append(answer)
        print(f"✅ 已添加: {question} => {answer}")


    def save_index(self):
        """
        保存 Faiss 索引到文件
        """
        faiss.write_index(self.index, self.index_file)
        print(f"💾 Faiss 索引已保存: {self.index_file}")


    def search(self, query, top_k=3):
        """
        搜索最相似的问题，并返回匹配结果
        """
        if len(self.questions) == 0:
            return "❌ 索引为空，请先添加数据！"

        query_vector = np.array([self.model.encode(query)], dtype="float32")
        distances, indices = self.index.search(query_vector, top_k)

        results = []
        for j, i in enumerate(indices[0]):
            if i < len(self.questions):  # 确保索引有效
                results.append({
                    "question": self.questions[i],
                    "answer": self.answers[i],
                    "score": float(distances[0][j])
                })
        
        return results

