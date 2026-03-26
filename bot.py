import ccxt
import pandas as pd

def analyze():
    print("--- 🔍 نظام CleanWave Alpha: جاري الفحص المستقل ---")
    try:
        exchange = ccxt.binance()
        bars = exchange.fetch_ohlcv('BTC/USDT', timeframe='15m', limit=100)
        df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        
        # حساب EMA يدوياً (بدون مكتبات خارجية)
        df['ema_8'] = df['close'].ewm(span=8, adjust=False).mean()
        df['ema_21'] = df['close'].ewm(span=21, adjust=False).mean()
        
        price = df['close'].iloc[-1]
        ema8 = df['ema_8'].iloc[-1]
        ema21 = df['ema_21'].iloc[-1]
        
        print(f"💰 السعر الحالي: {price}")
        print(f"📊 EMA 8: {round(ema8, 2)} | EMA 21: {round(ema21, 2)}")
        
        if ema8 > ema21:
            print("🚀 النتيجة: اتجاه صاعد (CleanWave Alpha)")
        else:
            print("📉 النتيجة: اتجاه هابط أو عرضي")
            
    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

if __name__ == "__main__":
    analyze()
