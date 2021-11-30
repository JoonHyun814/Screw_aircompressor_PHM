<!DOCTYPE html>
<html>
  <body>
    <h1>Screw air compressor PHM</h1>
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
          <li><h3>CNN_LSTM AE</h3></li>
            <p>
              encoding은 CNN으로, decoding은 LSTM을 사용한 CNN_LSTM AE의 계략도 입니다.
            </p>
        </ul>
      <h2><li>Perfomance test with reconstruct error</li></h2>
        <ul>
          <li><h3>Loss(MAE)</h3></li>
          <li><h3>anomaly score</h3></li>
        </ul>
    </ol>
  </body>
</html>
