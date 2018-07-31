# Algorithmic-Paper-Trading-Bot
The idea:
- Bollinger Bands are good at determining when the market may bounce back or when it may crash
  - However, by itself, it's "sell when it hits the upper band" or "buy when it hits the lower band"
  - What if when it hits the upper band it keeps on rising? What if when it hits the lower band it keeps on dropping?
- The Aroon Indicator is good at describing when a trend is continuing or when it will flip
- Combining the data from Bollinger Bands and from Aroon, this bot shoud be able to hold on to indexs and only sell once it hits the uppr Bollnger Band and the Aroon's up goes down.
  - It should also be able to buy once the index has hit the lower Bollinger and the Aroon's down goes up.
