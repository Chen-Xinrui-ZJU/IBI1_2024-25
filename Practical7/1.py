import re
import sys

# 读取 fasta 文件
fasta_file = r'F:\^Course Material\IBI1\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'

try:
    with open(fasta_file, "r") as file:
        text = file.read()
except FileNotFoundError:
    print(f"Error: File '{fasta_file}' not found.")
    sys.exit(1)

# 正则表达式提取基因名和序列
all_genes = re.findall(r'>.*?gene:(\S+).*?\n([A-Z\n]+)', text)

# 用户输入剪切供体/受体组合
DA = input("Enter the splice donor/acceptor combination (GTAG, GCAG, ATAC): ").strip().upper()

# 剪切供体/受体组合映射
donor_acceptor_map = {
    'GTAG': ('GT', 'AG'),
    'GCAG': ('GC', 'AG'),
    'ATAC': ('AT', 'AC')
}

# 判断输入是否有效
if DA not in donor_acceptor_map:
    print("Invalid input. Please enter one of: GTAG, GCAG, ATAC.")
    sys.exit(1)

donor, acceptor = donor_acceptor_map[DA]
output_file = rf'F:\^Course Material\IBI1\IBI1_2024-25\Practical7\{DA}_spliced_genes.fa'

# 处理基因序列
with open(output_file, "w") as newfile:
    for gene, sequence in all_genes:
        # 去除换行符，拼接完整的序列
        sequence_text = sequence.replace("\n", "")

        # 查找所有剪切片段
        splice_sites = re.findall(f"{donor}[A-Z]*?{acceptor}", sequence_text)

        # 统计含有 TATA box 的剪切片段
        tata_count = sum(len(re.findall(r'TATA[AT]A[AT]', splice_seq)) for splice_seq in splice_sites)

        # 只输出包含 TATA box 的剪切片段
        if tata_count > 0:
            newfile.write(f">{gene}\t{tata_count}\n{sequence_text}\n")

print(f"Process complete! Results saved in {output_file}")
