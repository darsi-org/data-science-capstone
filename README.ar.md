<div dir="rtl">

# المشروع الختامي: إيه اللي بيتنبّأ بطالب متعثر؟


> **ملخص درسي قصير عن قصد.** الدرس في التطبيق بيعرض خطوات ضغط مختصرة. الـ README ده بيحفظ الأوامر الكاملة وإصلاح الأخطاء والخلفية لكل مرحلة — افتح قسم **المرحلة N** لما تحتاج تفاصيل.

استخدم مجموعة بيانات طلاب عامة عشان تستكشف الحدود، وتغلب خط أساس بسيط بتحقق متقاطع صادق، وتبلغ عن عدم اليقين بالـ bootstrap، وتفحص العدالة بين المجموعات، وتكتب مذكرة من صفحتين مدير مدرسة يقدر يستخدمها.

[English](README.md)

## هتقدر تعمل إيه

- تشغّل أدوات حقيقية مجانية من اللابتوب أو Codespaces
- تخلّص خمس مراحل، كل مرحلة ليها فحص تقدر تتأكد منه بنفسك
- تطلع بقطعة بورتفوليو: تقرير أو عرض أو أداة بإصدار v1.0
- **درسي مش بيشغّل كودك أبدًا** — بيقرا الرابط وملف الفحص وبمراجعة استشارية

## ثبّت مرة واحدة

### ويندوز

1. ثبّت Python 3.12: افتح PowerShell واكتب `winget install Python.Python.3.12`
2. ثبّت Git: `winget install Git.Git`
3. ثبّت VS Code من https://code.visualstudio.com مجانًا
4. على GitHub افتح https://github.com/darsi-org/data-science-capstone واضغط **Use this template** عشان تعمل نسختك. وبعدين اعمل Clone لنسختك أنت، مش نسخة darsi-org: `git clone https://github.com/<your-username>/data-science-capstone.git`
5. افتح PowerShell جديد، وادخل الفولدر بـ `cd data-science-capstone`، وشغّل السطور دي واحد واحد:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python check.py
   ```

   لو PowerShell قال إن تشغيل السكربتات متقفل على الجهاز ده، مش محتاج تغيّر أي إعداد: استخدم Command Prompt وشغّل `.venv\Scripts\activate.bat` بداله، أو من غير تفعيل ابدأ كل أمر بـ `.venv\Scripts\python` (مثلًا `.venv\Scripts\python -m pip install -r requirements.txt`، وبعدين `.venv\Scripts\python check.py`).

### ماك

1. ثبّت Homebrew من https://brew.sh لو مش متثبت
2. ثبّت Python وGit: `brew install python@3.12 git`
3. ثبّت VS Code من https://code.visualstudio.com
4. على GitHub افتح https://github.com/darsi-org/data-science-capstone واضغط **Use this template**، وبعدين اعمل Clone لنسختك: `git clone https://github.com/<your-username>/data-science-capstone.git`
5. في Terminal ادخل الفولدر بـ `cd data-science-capstone` وشغّل:

   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python check.py
   ```

### Codespaces / Colab

معندكش كمبيوتر؟ استخدم GitHub Codespaces، حتى من لابتوب مستعار: افتح نسختك → **Code** → **Codespaces** → **Create codespace**. Python وGit موجودين أصلًا. في الـ terminal بتاعه شغّل:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python check.py
```

أو استخدم Google Colab للدفتر اللي في notebooks/: افتح `https://colab.research.google.com/github/<your-username>/data-science-capstone/blob/main/notebooks/01_explore.ipynb` (اسم المستخدم بتاعك مكان `<your-username>`)، حط عنوان نسختك في أول خلية وشغّلها. الخلية دي بتعمل Clone لنسختك وبتدخل فيها. Colab بيشتغل على نسخة خاصة بيه، فنزّل اللي عملته (figures/ وresults/) وضيفه للريبو بتاعك على GitHub (**Add file** → **Upload files**).

متصفح الموبايل يكفي تقرا النتائج.

## البداية

اضغط **Use this template** على https://github.com/darsi-org/data-science-capstone، Clone نسختك، وبعدين اتبع المرحلة ١.

## المراحل

### m1: استكشف البيانات وحدودها (3 ساعات)

#### ليه ده مهم
قبل أي نموذج، لازم تعرف مين في البيانات ومين ناقص. بيانات اتجمعت في ٢٠٠٥–٢٠٠٦ من مدرستين في البرتغال (واتنشرت في ٢٠٠٨) مش عن طلاب مصريين النهارده.

#### الأدوات للمرحلة دي
- **ucimlrepo** — بينزّل مجموعة UCI لأداء الطلاب. هتجيبه من: pip install -r requirements.txt
- **Jupyter / Colab** — بيشغّل دفتر الاستكشاف في المتصفح. هتجيبه من: https://colab.research.google.com or Codespaces

#### اعمل كده
1. جهّز نسختك زي **ثبّت مرة واحدة** (نسختك أنت، مش نسخة darsi-org).
2. شغّل `python fetch_data.py`. بيحفظ data/students.csv (٦٤٩ طالب ثانوي برتغالي). وأول خلية في الدفتر بتعمل كده برضه لو الملف مش موجود.
3. افتح notebooks/01_explore.ipynb في VS Code أو Colab وشغّل أول خلية الأول: بتنقلك لأول فولدر في الريبو، فـ `plt.savefig("figures/<name>.png")` بيحفظ في فولدر figures/ بتاع الريبو، اللي check.py بيدوّر فيه. اعمل خمسة رسوم: توزيع G3 (موجود في الدفتر كمثال)، والغياب، ووقت المذاكرة مقابل G3، واتنين من اختيارك.
4. اكتب LIMITS.md: البيانات اتجمعت فين وإمتى، ومين ناقص، وليه مش عن طلاب مصريين.
5. زوّد رابط Colab أو الدفتر في README.md. شغّل python check.py --milestone m1.

#### هتبقى خلصت لما
- figures/ فيه خمسة PNG
- LIMITS.md مكتوب
- m1 ناجحة ورابط الدفتر بيفتح

#### لو حاجة وقفت
- **تحميل ucimlrepo فشل** → اتأكد من النت؛ حاول تاني. رقم المجموعة ٣٢٠.
- **الـ kernel ناقص** → اختار مفسّر .venv في VS Code، أو استخدم Colab
- **check.py عايز خمسة رسوم** → شغّل أول خلية في الدفتر، وبعدين احفظ بـ `plt.savefig("figures/<name>.png")`. الصور مكانها figures/ في أول الريبو، مش notebooks/figures/

#### إيه اللي لازم تفهمه
تقدر توصف شكل مجموعة بيانات وتقول بوضوح مين مش ممثّل فيها.

**المطلوب تسليمه:** رابط الدفتر، وخمسة رسوم، وLIMITS.md، وdarsi-check.json بيجتاز m1.

### m2: خط أساس، وبعدين تلات نماذج (4 ساعات)

#### ليه ده مهم
نموذج معقّد بالكاد بيغلب «تنبّأ بالمتوسط» مش تقدّم. تقسيم ببذرة وتحقق متقاطع بيخلوك صادق.

#### الأدوات للمرحلة دي
- **scikit-learn** — أقرب جيران وانحدار خطي وشجرة قرار وتحقق متقاطع. هتجيبه من: موجود في requirements.txt

#### اعمل كده
1. قسّم مرة: ٨٠٪ تدريب و٢٠٪ اختبار، وrandom_state ثابت. متبصش على بيانات الاختبار لسه.
2. قرّر هتستخدم G1 وG2 (درجات الترم الأول والترم التاني) كخصائص ولا لأ. لو استخدمتهم، نموذجك يبقى فحص بعد الترم التاني: G3 قريبة جدًا منهم، فهيغلب خط الأساس بسهولة. ومن غيرهم، يبقى إنذار بدري قبل ما يبقى فيه أي درجات. اكتب اختيارك وليه تحت جدول المقاييس.
3. خط الأساس: تنبّأ بمتوسط التدريب لـ G3 للكل. سجّل الـ MAE بتاعه، بتحقق متقاطع زي النماذج، كـ baseline_mae في results/cv.json.
4. درّب أقرب جيران وانحدار خطي وشجرة قرار بتحقق متقاطع ٥ طيات على بيانات التدريب بس. سجّل MAE لكل واحد.
5. خلي test_used تساوي false في results/cv.json. شغّل python check.py --milestone m2.

#### مثال محلول: تحقق متقاطع ٥ طيات ببذرة
شغّله من أول فولدر في المستودع (في الدفتر، بعد أول خلية). النسخة دي من غير G1 وG2، يعني إنذار بدري. لو هتستخدمهم، شيلهم من قايمة الأعمدة اللي بتتشال، بس G3 لازم تتشال دايمًا: دي الإجابة.

```python
import json
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

SEED = 42
df = pd.read_csv("data/students.csv")
X = pd.get_dummies(df.drop(columns=["G1", "G2", "G3"]), drop_first=True)  # words become 0/1 columns
y = df["G3"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)  # test: not yet

folds = KFold(n_splits=5, shuffle=True, random_state=SEED)
models = {
    "baseline": DummyRegressor(strategy="mean"),  # the training mean for everyone
    "knn": make_pipeline(StandardScaler(), KNeighborsRegressor(n_neighbors=10)),
    "linear": LinearRegression(),
    "tree": DecisionTreeRegressor(max_depth=4, random_state=SEED),
}
cv_mae = {}
for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=folds, scoring="neg_mean_absolute_error")
    cv_mae[name] = round(float(-scores.mean()), 3)  # scikit-learn reports MAE as a negative number
print(cv_mae)
with open("results/cv.json", "w") as f:
    json.dump({"seed": SEED, "baseline_mae": cv_mae["baseline"], "cv_mae": cv_mae, "test_used": False}, f, indent=2)
```

`cross_val_score` بيقسم جزء التدريب لـ ٥ طيات، ويدرّب على ٤ ويقيّم على الخامسة، خمس مرات؛ وبيانات الاختبار مبتتلمسش. أقرب جيران بيقيس مسافات، فالـ pipeline بتاعه بيوحّد مقياس كل عمود الأول.

#### هتبقى خلصت لما
- results/cv.json فيه seed وbaseline_mae وtest_used false
- جدول المقاييس بيقول G1 وG2 خصائص ولا لأ، وليه
- m2 ناجحة

#### لو حاجة وقفت
- **الدرجات مثالية (MAE قرب صفر)** → غالبًا قيّمت على التدريب؛ استخدم cross_val_score على التدريب بس
- **أرقام مختلفة كل مرة** → ثبّت random_state في كل حتة واحفظه كـ seed في cv.json

#### إيه اللي لازم تفهمه
تقدر تقارن النماذج بخط أساس بسيط بتقسيم ببذرة، من غير ما تبص على بيانات الاختبار.

**المطلوب تسليمه:** results/cv.json، وجدول المقاييس مع جملة عن G1 وG2، وdarsi-check.json بيجتاز m2.

### m3: متأكد لحد فين؟ الـ bootstrap (3 ساعات)

#### ليه ده مهم
MAE واحد بيخفي قد إيه ممكن يتحرك. فترة bootstrap بتورّي قد إيه، والفترة المقترنة للفرق بتورّي إذا كان نموذجك غلب خط الأساس فعلًا.

#### الأدوات للمرحلة دي
- **numpy / pandas** — بيعيد عيّنة صفوف الاختبار ١٠٠٠ مرة. هتجيبه من: موجود في requirements.txt

#### اعمل كده
1. قيّم نموذجك المختار مرة واحدة على بيانات الاختبار. احفظ MAE للاختبار.
2. Bootstrap: أعد عيّنة صفوف الاختبار ١٠٠٠ مرة مع الإرجاع. في كل مرة، احسب MAE نموذجك وMAE خط الأساس على نفس الصفوف، وسجّل MAE خط الأساس ناقص MAE النموذج. المئين ٢٫٥ والمئين ٩٧٫٥ لكل واحد هما فترة ٩٥٪: ci95 (نموذجك)، وbaseline_ci95 (خط الأساس)، وdiff_ci95 (الفرق).
3. اقرا diff_ci95. لو كلها فوق الصفر، نموذجك غلب خط الأساس فعلًا. لو فيها الصفر، بيانات الاختبار دي مش قادرة تفرّق بينهم: قول كده. متحكمش بإن ci95 وbaseline_ci95 متداخلين ولا لأ: فترتين منفصلتين ممكن يتداخلوا حتى لو نموذج أحسن من التاني بشكل ثابت. اكتب جملة عن اللي diff_ci95 بتقوله، واحفظ results/test.json.
4. شغّل python check.py --milestone m3.

#### مثال محلول: bootstrap مقترن
شغّله بعد مثال m2، بنفس SEED ونفس التقسيم، عشان صفوف الاختبار تبقى اللي عمرك ما استخدمتها.

```python
import numpy as np

best = models["linear"].fit(X_train, y_train)  # the model you chose in m2, trained on all of the training part
err_model = np.abs(y_test.to_numpy() - best.predict(X_test))
err_base = np.abs(y_test.to_numpy() - y_train.mean())

rng = np.random.default_rng(SEED)
rows = rng.integers(0, len(y_test), size=(1000, len(y_test)))  # 1,000 resamples of the test rows
model_mae = err_model[rows].mean(axis=1)  # each resample scores both on the SAME rows
base_mae = err_base[rows].mean(axis=1)
diff = base_mae - model_mae  # above 0: the model did better

def ci95(values):
    return [round(float(x), 3) for x in np.percentile(values, [2.5, 97.5])]

result = {"seed": SEED, "test_mae": round(float(err_model.mean()), 3), "baseline_test_mae": round(float(err_base.mean()), 3),
          "ci95": ci95(model_mae), "baseline_ci95": ci95(base_mae), "diff_ci95": ci95(diff)}
print(result)
with open("results/test.json", "w") as f:
    json.dump(result, f, indent=2)
```

ليه بنقرنهم: الطالب اللي سهل التنبؤ بيه سهل على الاتنين، فالـ MAE بتاع الاتنين بيطلع وينزل مع بعض من إعادة عيّنة للتانية. الفرق بينهم بيتحرك أقل مما الفترتين جنب بعض بيوحوا، وعشان كده التداخل اختبار غلط.

#### هتبقى خلصت لما
- results/test.json فيه ci95 وbaseline_ci95 وdiff_ci95
- m3 ناجحة

#### لو حاجة وقفت
- **الفترة رقم واحد** → احفظ الطرفين، زي [low, high]
- **الـ bootstrap بياخد وقت طويل** → ١٠٠٠ إعادة عيّنة لمتجه الاختبار تكفي؛ متعيدش التدريب جوّه الحلقة
- **ci95 وbaseline_ci95 متداخلين، بس diff_ci95 كلها فوق الصفر** → ده طبيعي. صدّق diff_ci95: الاتنين اتقيّموا على نفس الطلاب.

#### إيه اللي لازم تفهمه
تقدر تبلغ عن عدم اليقين، مش درجة واحدة بس، وتستخدم فترة مقترنة عشان تقول إذا كان نموذجين مختلفين فعلًا.

**المطلوب تسليمه:** results/test.json (فيه diff_ci95)، وجملة بتقول فترة الفرق كلها فوق الصفر ولا لأ، وdarsi-check.json بيجتاز m3.

### m4: هل هو عادل؟ الأخطاء حسب المجموعة (3 ساعات)

#### ليه ده مهم
المتوسط ممكن يخفي مجموعة النموذج بيفشل معاها. المدارس لازم تشوف كده قبل ما تثق في درجة.

#### الأدوات للمرحلة دي
- **pandas groupby** — MAE حسب المدرسة وحضر/ريف والجنس. هتجيبه من: built into your stack

#### اعمل كده
1. احسب MAE للاختبار حسب المدرسة، وحسب حضر/ريف، وحسب الجنس. احفظ أرقام قبل في results/groups.json.
2. لاقي أكبر فجوة واقتراح ليه (أمثلة أقل؟ تصحيح مختلف؟).
3. جرّب إصلاح واحد (وزّع وزن أكبر للمجموعة الأصغر، أو شيل خاصية وسيطة) واحفظ أرقام بعد.
4. شغّل python check.py --milestone m4.

#### هتبقى خلصت لما
- results/groups.json فيه before وafter
- m4 ناجحة

#### لو حاجة وقفت
- **مجموعة فيها صفر صفوف** → ادمج المستويات النادرة أو اكتب «n صغير» بدل MAE مزيف
- **الإصلاح خلّى المتوسط أسوأ والفجوة أسوأ** → قول كده بصدق؛ مش كل إصلاح بيساعد. جرّب حاجة تانية.

#### إيه اللي لازم تفهمه
تقدر تقيس فجوات الخطأ بين المجموعات وتجرّب إصلاح واحد من غير ما تخفي المقايضة.

**المطلوب تسليمه:** results/groups.json، وملاحظة قصيرة عن الفجوة، وdarsi-check.json بيجتاز m4.

### m5: مذكرة مدرسة تقدر تستخدمها (3 ساعات)

#### ليه ده مهم
المهارة مش الدفتر؛ النصيحة اللي مدير المدرسة يقدر يتحرك بيها من غير ما يتضلل.

#### الأدوات للمرحلة دي
- **GitHub Actions** — بيعيد تشغيل الدفاتر من الأول للآخر. هتجيبه من: workflow in the starter
- **GitHub Release** — نسخة ثابتة من المذكرة والكود. هتجيبه من: tag v1.0

#### اعمل كده
1. اكتب MEMO.md (إنجليزي أو عربي، صفحتين بالكتير): السؤال، وحدود البيانات، وأحسن نموذج مقابل خط الأساس مع فترة الفرق، وفجوات العدالة، وتلاتة توصيات، وإيه المدرسة لازم متعملوش.
2. قول إيه البيانات المحلية، بموافقة، اللي هتحتاجها عشان تعمل كده صح في مصر.
3. ارفع عشان Actions يشغّل الدفاتر. حط إصدار v1.0. شغّل python check.py --milestone m5.
4. اشرح المشروع كله بكلامك على درسي.

#### هتبقى خلصت لما
- MEMO.md بيقول إيه متعملوش
- v1.0 موجود وm5 ناجحة

#### لو حاجة وقفت
- **Actions بيفشل وهو بيجيب البيانات** → أول خلية في الدفتر بتجيبها لو data/students.csv مش موجود؛ ولو موقع UCI واقع، اعمل commit لـ data/students.csv (ترخيصها CC BY 4.0 بيسمح بكده)
- **المذكرة أطول من صفحتين** → قصّر الرسوم؛ اربط الدفتر بدلًا منها

#### إيه اللي لازم تفهمه
تقدر تحوّل مشروع نمذجة لنصيحة حذرة بتسمّي الحدود وبرفض الاستخدامات المؤذية.

**المطلوب تسليمه:** MEMO.md، وتشغيل Actions أخضر، وv1.0، وdarsi-check.json بيجتاز m5، وشرحك.

## الفحص

شغّل `python check.py` أو `python check.py --milestone m2`. بيقرا الملفات بس، بيكتب `darsi-check.json`، وبيطبّع بالإنجليزي والعربي. مش بيرفع حاجة.

## المراجعة على درسي

ابعت رابط الريبو و`darsi-check.json` مع كل مرحلة على درسي. درسي بيقرا آخر تشغيل Actions والإصدار من واجهة GitHub العامة، بيضيف مراجعة استشارية بالذكاء الاصطناعي، وبعدين معلّمك أو فريق درسي بيراجع. **درسي مش بيشغّل كودك.**

## الترخيص

MIT — شوف [LICENSE](LICENSE).

</div>
