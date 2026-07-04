# تشغيل البوت كخدمة دائمة (systemd)

بعد ما تسوي أول تشغيل (`bash start.sh`) وتدخل التوكن والـ SUDO ID بنجاح، وقف البوت (Ctrl+C) وسوّي التالي:

## 1. انسخ ملف الخدمة
```
sudo cp waad-bot.service /etc/systemd/system/waad-bot.service
```

> إذا رفعت المشروع بمسار مختلف عن `/home/ubuntu/bot/bmqa`، عدّل `WorkingDirectory` و`ExecStart` بملف `waad-bot.service` قبل النسخ.

## 2. فعّل الخدمة
```
sudo systemctl daemon-reload
sudo systemctl enable waad-bot.service
sudo systemctl start waad-bot.service
```

## 3. أوامر مفيدة
- تشيك الحالة: `sudo systemctl status waad-bot.service`
- متابعة اللوق مباشرة: `journalctl -u waad-bot.service -f`
- إعادة تشغيل: `sudo systemctl restart waad-bot.service`
- إيقاف: `sudo systemctl stop waad-bot.service`

## المميزات
- البوت يشتغل تلقائي عند إعادة تشغيل السيرفر.
- لو البوت طاح لأي سبب، systemd يعيد تشغيله تلقائي بعد 5 ثواني (`Restart=on-failure`).
- ما تحتاج screen أو تبقي الـ SSH مفتوح.
