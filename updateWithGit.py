import os
from dotenv import load_dotenv
import requests
from git import Repo

# GitHub API 設置
github_api_url = "https://api.github.com"
load_dotenv()
github_token = os.getenv('GITHUB_TOKEN')
headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}


def create_github_repo(repo_name):
    """使用 GitHub API 創建新的遠程倉庫"""
    data = {"name": repo_name, "auto_init": True}
    response = requests.post(f"{github_api_url}/user/repos", headers=headers, json=data)
    if response.status_code == 201:
        return response.json()["clone_url"]
    else:
        raise Exception(f"Failed to create repo: {response.content}")

def setup_git_config(repo):
    """設置 Git 配置"""
    with repo.config_writer() as git_config:
        git_config.set_value('user', 'name', 'Hinarin2017')
        git_config.set_value('user', 'email', 'b812110011@example.com')


def setup_local_repo(repo_name, remote_url):
    """設置本地倉庫並連接到遠程"""
    local_path = os.path.join(os.getcwd(), repo_name)
    # 在 URL 中添加 token
    auth_remote_url = remote_url.replace('https://', f'https://{github_token}@')
    repo = Repo.clone_from(auth_remote_url, local_path)
    setup_git_config(repo)
    return repo


def create_new_branch(repo, branch_name):
    """創建新分支"""
    new_branch = repo.create_head(branch_name)
    new_branch.checkout()


def add_file_and_commit(repo, file_name, content):
    """添加新文件並提交"""
    file_path = os.path.join(repo.working_dir, file_name)
    with open(file_path, 'w') as f:
        f.write(content)
    repo.index.add([file_path])
    repo.index.commit(f"Add {file_name}")


def push_changes(repo, branch_name):
    """推送更改到遠程倉庫"""
    origin = repo.remote('origin')
    origin.push(branch_name)


# 使用示例
if __name__ == "__main__":
    repo_name = "my_new_repo2"
    branch_name = "new-feature"

    # 創建新的 GitHub 倉庫
    remote_url = create_github_repo(repo_name)
    print(f"Created new repo: {remote_url}")

    # 設置本地倉庫
    repo = setup_local_repo(repo_name, remote_url)
    print(f"Local repo set up at: {repo.working_dir}")

    # 創建新分支
    create_new_branch(repo, branch_name)
    print(f"Created new branch: {branch_name}")

    # 添加文件並提交
    add_file_and_commit(repo, "README.md", "# My New Project\nThis is a test project.")
    print("Added README.md and committed")

    # 推送更改
    push_changes(repo, branch_name)
    print(f"Pushed changes to {branch_name}")