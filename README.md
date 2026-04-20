# Screw Aircompressor PHM

**딥러닝 기반 철도차량 나사식 공기압축기 예지보전 (PHM)**

[![논문 1](https://img.shields.io/badge/논문1-철도차량_시뮬레이션_연구-0052CC?style=flat)](https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE10584865)
[![논문 2](https://img.shields.io/badge/논문2-LSTM_CNN_이상감지-0052CC?style=flat)](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10896480)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://tensorflow.org)

---

## 배경

철도차량 공기압축기는 고장 전에 교체해야 하지만, 고정 주기 교체 방식은 비효율적입니다. 너무 이르면 비용 낭비, 너무 늦으면 고장 위험이 있습니다. 이 프로젝트는 **데이터 기반 PHM(Prognostics and Health Management)** 방식으로 이상을 조기 감지하고 잔여 수명을 예측합니다.

건국대학교 학부연구생 과정에서 수행했으며, **논문 2편**이 DBpia에 게재되었습니다.

---

## 접근 방법

### 1단계 — 결함 데이터 시뮬레이션 (MATLAB)

실제 공기압축기 결함 데이터는 수집이 어렵습니다. 대신:
- 2단 피스톤 공기압축기의 고장 사례 논문을 분석
- MATLAB으로 각 부품별 정상/결함 상태의 압력·온도·진동 등 상태량 시뮬레이션
- 실제 고장 사례를 기반으로 결함 발생 시 상태량 변화 예측

### 2단계 — 이상 감지 (Autoencoder)

**정상 데이터만으로 학습** — 정상 패턴 재구성을 학습하며, 이상 입력 시 재구성 오차가 높아집니다.

4가지 Autoencoder 아키텍처를 비교 평가했습니다:

| 모델 | 아키텍처 |
|------|---------|
| `LSTM_AE` | LSTM 인코더 → LSTM 디코더 |
| `CNN_AE` | 1D-CNN 인코더 → 1D-CNN 디코더 |
| `LSTM_CNN_AE` | LSTM 인코더 → CNN 디코더 |
| `CNN_LSTM_AE` | CNN 인코더 → LSTM 디코더 |

### 3단계 — 잔여 수명 예측 (LSTM)

별도의 LSTM 회귀 모델(`LSTM_predict`)이 재구성 오차 신호를 입력으로 받아 고장까지 남은 사이클 수를 예측합니다.

---

## 저장소 구조

```
Screw_aircompressor_PHM/
├── codes/
│   ├── preprocess.py            # 데이터 전처리 파이프라인
│   ├── train_AE model.ipynb     # Autoencoder 학습
│   ├── test_AE model.ipynb      # 이상 감지 평가
│   └── LSTM_predict_model.ipynb # 잔여 수명 예측
└── models/
    ├── CNN_AE_1.h5
    ├── LSTM_AE_1.h5
    ├── CNN_LSTM_AE_1.h5
    ├── LSTM_CNN_AE_1.h5
    └── LSTM_predict_1.h5
```

---

## 논문

1. **철도차량 2단 피스톤 공기압축기의 시뮬레이션 연구**
   [→ DBpia](https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE10584865)
   MATLAB을 이용한 2단 피스톤 공기압축기 각 부품별 상태량 시뮬레이션 연구.

2. **LSTM과 CNN 기반의 공기압축기 이상감지**
   [→ DBpia](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10896480)
   LSTM · CNN 기반 Autoencoder를 활용한 공기압축기 이상감지. 선박 공기압축기 선행 연구를 철도차량 데이터에 적용·확장.

---

## 기술 스택

- **Python** — TensorFlow/Keras, NumPy, pandas
- **MATLAB** — 공기압축기 상태량 물리 시뮬레이션
- **모델** — LSTM, 1D-CNN, 하이브리드 Autoencoder 아키텍처
