# 프로젝트 소개 
이 프로젝트는 python 기반 오픈소스(3d-bin-packing-problem) 알고리즘을 활용하여 물류를 컨테이너에 적재하는 시각화 알고리즘을 사용하여 다양한 창고물류 입출력 시스템을 해상 물류 컨테이너 시스템에 효과적으로 적용하여 시뮬레이션하는 것을 목표로 한다. 3개의 고정 크기의 물류 컨테이너에 크기, 무게를 고려하여 분배된 물류를 적재하고, 적재 가능할 경우 이미지로 불가능할 경우 적재 불가 항목으로 결과를 나타내어 준다. 이를 위해 "쿠버네티스" 환경에서 운영하여 대량의 시뮬레이션을 실시할 수 있으며, 이를 통해 빠르고 효율적으로 인프라를 관리하고 컨테이너 물류 시스템을 안정적으로 운영하고자 한다. 


## 작품 기능
ㅇ 효율성있는 물류 선적 알고리즘 <br>
ㅇ 물류 관리 소프트웨어를 통한 시뮬레이션 데이터 입출력    <br>
ㅇ 실제 선박에 선적되는 수천톤의 수하물에 해당하는 컨테이너 물류 입출력  <br>
   ㅇ 대량의 데이터가 담긴 csv 파일 입력 <br>
   ㅇ 데이터 수기 입력 <br>
ㅇ 입력 데이터에 따른 물류 선적 시뮬레이터 동작과 결과물 출력  <br>
ㅇ 쿠버네티스를 사용한 마이크로서비스 운영/관리

## 프로젝트 시나리오
![image](https://github.com/SmGirls/SmGirlsDocker/assets/79689822/a28dcbc5-a072-4c9f-bb36-df92c9b95a65)


## SW 구성도
![image](https://github.com/SmGirls/SmGirlsDocker/assets/79689822/d842325d-ddcf-4a87-9e56-d1cc44c55450)

## PV 와 PVC 배치도
![image](https://github.com/SmGirls/SmGirlsDocker/assets/79689822/7252f82c-f18e-405e-8e51-14b23525d82d)

## 프로젝트 영상 요약 소개
[유튜브 링크](https://www.youtube.com/watch?v=VAB8FhqrSd4)

---

# Simul-Back

## Add your files

```
git remote add origin https://lab.hanium.or.kr/23_HP027/flask_binpacking.git
git clone https://lab.hanium.or.kr/23_HP027/flask_binpacking.git
cd Simul-Back
git branch -M main
git push -uf origin main

```
## Component
- app.py : 우리의 의도대로 돌아가야하지만.. 약간의 error가 발생하는 코드 ... (수정 필요요)

## How to build
```
# requirements install
pip install -r requirements.txt 
# 실행 
python app.py
```
