# Simple Dockerfile



## Getting started
- 3D Bin Packing을 해주는 파이썬 코드를 토대로 컨테이너에 물류 적재
[3d-bin-packing-problem](https://github.com/ylmz-dev/3d-bin-packing-problem)


## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
git remote add origin https://lab.hanium.or.kr/23_HP027/simple-dockerfile.git
git clone https://lab.hanium.or.kr/23_HP027/simple-dockerfile.git
cd simple-dockerfile
git branch -M main
git push -uf origin main

```
## Component
- Dockerfile
- main.py : 우리의 의도대로 돌아가야하지만.. 약간의 error가 발생하는 코드 ... (수정 필요요)
- test.py : 간단한 기능이 들어가 있음 

## Dockerfile
```
# Dockerfile Build
docker build . -t 3D-image:0.1
# 실행 및 포트포워딩
docker run --name kch-nginx -d -p 8080:80 3d-image:0.1
```