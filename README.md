<!DOCTYPE html>
<html>
  <body>
    <h1>Screw air compressor PHM</h1>
    <p>
      이 프로젝트에서는 철도차량의 공기압축기의 경재성을 위해 정비주기를 줄이고자 CBM(상태기반정비)를 하기 위하여 이상을 감지 하고, 또 나아가서 언제 이상이 발생할지를 머신러닝을 통하여 예측하고자합니다. readme에서는 간단한 이론만 기제되어 있으며, 이에 대한 소스코드는 ipynb파일에 있습니다.
    </p>
    <ol>
      <h2><li>Data prepocessing</li></h2>
        <ul>
          <li><h3>normaliztion</h3></li>
            <p>
              data의 최대, 최소치를 0~1로 바꾸어 줍니다.
            </p>
          <li><h3>Moving window</h3></li>
            <p>
              무한한 시계열성을 가지고 있는 data를 모델에 input할 수 있도록 일정한 시계열 길이를 가지는 window 조각들로 나누어 줍니다.
            </p>
          <img src="https://user-images.githubusercontent.com/79820509/143999032-fc1d8a26-81aa-45fc-918c-3b2d30737469.png" alt="" width="90%"><br>
        </ul>
      <h2><li>Auto encoder</li></h2>
        <p>
          auto encoder란 data를 encoder를 통하여 압축한 후, 다시 decoder를 통해 복원하였을 때, 얼마나 잘 복원하였는가를 보고 이상을 탐지 합니다. 만약 복원한 데이터가 원본 데이터와 큰 차이가 있다면 모델은 이것을 이상이 있다고 판단 합니다. encoder와 decoder에 어떠한 layer가 사용되었는 지에 따라 LSTM_AE, CNN_AE, VAE등으로 불리게 됩니다.
        </p>
        <ul>
          <li><h3>LSTM AE</h3></li>
            <p>
              encoding과 decoding을 모두 LSTM을 사용한 LSTM AE의 계략도 입니다.
            </p>
          <img src="https://user-images.githubusercontent.com/79820509/143997924-aca3b90d-49aa-40c4-b005-c8568781ecd0.png" alt="" width="90%"><br>
          <li><h3>CNN_LSTM AE</h3></li>
            <p>
              CNN_LSTM AE는 encoding은 CNN으로, decoding은 LSTM을 사용합니다. 아래는 CNN encoder의 계략도 입니다.
            </p>
          <img src="https://user-images.githubusercontent.com/79820509/143998308-a3cc70b7-0adf-4906-835a-9b6adebb8e8d.png" alt="" width="90%"><br>
        </ul>
      <h2><li>Perfomance test with reconstruct error</li></h2>
      성능을 평가 하기 위해서 reconstruct error를 MAE 방식과 데이터의 분포까지 고려한 anomaly score 방식으로 각각 구하여서 성능을 평가하였습니다. error가 낮은 것도 중요하지만, 그 error가 일정한 것도 중요하다고 판단하였기 때문에 error의 평균과 분산을 각각 계산하여 더 낮은 값이 더 좋은 모델이라 판단하였습니다. 이 방법을 사용하면 이상 데이터가 충분하지 않은 상황에서도 모델을 평가할 수 있습니다.
        <ul>
          <li><h3>Loss(MAE)</h3></li>
          <p>
            단순히 차(error)의 절대값(absolute)의 평균(mean)입니다.
          </p>
          <li><h3>anomaly score</h3></li>
          <p>
            평균과 공분산을 활용한 공식을 사용하며 loss가 어떻게 분포되어있는지에도 영향을 받습니다. 사용하는 feature 수가 많은 수록 MAE보다 뛰어난 test 성능을 보여줍니다.
          </p>
        </ul>
    </ol>
  </body>
</html>
