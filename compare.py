import os
import hashlib
import argparse
from collections import defaultdict

def normalize_line_endings(content):
    """将内容中的换行符统一为LF"""
    return content.replace(b'\r\n', b'\n').replace(b'\r', b'\n')

def compare_files_ignoring_line_endings(file1, file2):
    """比较两个文件，忽略换行符差异"""
    try:
        with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
            content1 = f1.read()
            content2 = f2.read()
            
            # 统一换行符后比较
            normalized1 = normalize_line_endings(content1)
            normalized2 = normalize_line_endings(content2)
            
            return normalized1 == normalized2
    except Exception as e:
        print(f"比较文件时出错: {e}")
        return False

def get_file_info(root_dir):
    """获取目录下所有文件的信息"""
    file_info = defaultdict(dict)
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(full_path, root_dir)
            
            # 计算文件大小和哈希
            try:
                file_size = os.path.getsize(full_path)
                with open(full_path, 'rb') as f:
                    content = f.read()
                    normalized_content = normalize_line_endings(content)
                    file_hash = hashlib.md5(normalized_content).hexdigest()
                
                file_info[rel_path] = {
                    'size': file_size,
                    'hash': file_hash,
                    'full_path': full_path
                }
            except Exception as e:
                print(f"处理文件 {rel_path} 时出错: {e}")
    
    return file_info

def compare_branches(branch1_dir, branch2_dir):
    """比较两个分支目录"""
    print("正在扫描文件...")
    files1 = get_file_info(branch1_dir)
    files2 = get_file_info(branch2_dir)
    
    all_files = set(files1.keys()) | set(files2.keys())
    
    results = {
        'identical': [],      # 完全相同的文件
        'different': [],      # 内容不同的文件
        'only_in_branch1': [], # 只在分支1中存在的文件
        'only_in_branch2': []  # 只在分支2中存在的文件
    }
    
    for rel_path in sorted(all_files):
        if rel_path in files1 and rel_path in files2:
            # 文件在两个分支中都存在
            if files1[rel_path]['hash'] == files2[rel_path]['hash']:
                results['identical'].append(rel_path)
            else:
                results['different'].append(rel_path)
        elif rel_path in files1:
            results['only_in_branch1'].append(rel_path)
        else:
            results['only_in_branch2'].append(rel_path)
    
    return results

def print_comparison_results(results, branch1_name="分支1", branch2_name="分支2"):
    """打印比较结果"""
    print("\n" + "="*60)
    print("比较结果汇总")
    print("="*60)
    
    print(f"\n相同的文件 ({len(results['identical'])}):")
    for file in results['identical'][:10]:  # 只显示前10个相同的文件
        print(f"  ✓ {file}")
    if len(results['identical']) > 10:
        print(f"  ... 还有 {len(results['identical']) - 10} 个相同的文件")
    
    print(f"\n不同的文件 ({len(results['different'])}):")
    for file in results['different']:
        print(f"  ✗ {file}")
    
    print(f"\n只在 {branch1_name} 中的文件 ({len(results['only_in_branch1'])}):")
    for file in results['only_in_branch1']:
        print(f"  + {file}")
    
    print(f"\n只在 {branch2_name} 中的文件 ({len(results['only_in_branch2'])}):")
    for file in results['only_in_branch2']:
        print(f"  - {file}")
    
    # 统计信息
    print("\n" + "="*60)
    total_files = len(results['identical']) + len(results['different']) + \
                  len(results['only_in_branch1']) + len(results['only_in_branch2'])
    print(f"文件总数: {total_files}")
    print(f"相同文件: {len(results['identical'])}")
    print(f"不同文件: {len(results['different'])}")
    print(f"独有文件: {len(results['only_in_branch1']) + len(results['only_in_branch2'])}")

def main():
    parser = argparse.ArgumentParser(description='比较两个项目分支的文件差异（忽略换行符）')
    parser.add_argument('branch1', help='第一个分支目录路径')
    parser.add_argument('branch2', help='第二个分支目录路径')
    parser.add_argument('--name1', help='第一个分支的名称', default='分支1')
    parser.add_argument('--name2', help='第二个分支的名称', default='分支2')
    
    args = parser.parse_args()
    
    if not os.path.isdir(args.branch1):
        print(f"错误: {args.branch1} 不是有效的目录")
        return
    
    if not os.path.isdir(args.branch2):
        print(f"错误: {args.branch2} 不是有效的目录")
        return
    
    print(f"比较项目分支:")
    print(f"  {args.name1}: {args.branch1}")
    print(f"  {args.name2}: {args.branch2}")
    
    results = compare_branches(args.branch1, args.branch2)
    print_comparison_results(results, args.name1, args.name2)

if __name__ == "__main__":
    main()