# نظام إدارة المكتبة (`library_manegment`)

نظام ويب لإدارة مكتبة كلية، مبني كتطبيق على إطار [Frappe](https://frappeframework.com/) (المستهدف الإصدار 15، وPython 3.10 أو أحدث). يفهرس المراجع، ويتتبع كل نسخة فعلية، ويعالج الاستعارة والإرجاع، ويسجل الغرامات والتلف. وتعرض واجهة Vue عامة صغيرة كتالوج الكتب.

> اسم التطبيق مكتوب `library_manegment` (تُرك كما هو لأن إعادة تسميته تغيّر مسارات الـ API التي تستخدمها الواجهة). أما الـ Module الداخلي فاسمه `library_management`.

[English](README.md) · [المشاكل المعروفة](docs/KNOWN_ISSUES.md)

## الميزات

* **الفهرسة:** الكتب والمجلات والأبحاث والرسائل العلمية ومشاريع التخرج والمواد الصوتية والمرئية والإلكترونية، مع المؤلفين والناشرين والتصنيفات.
* **النسخ الفعلية:** `Item Copy` لكل نسخة، بباركود خاص (`باركود المرجع-معرّف النسخة`) وحالة (متاح / غير متاح / تالف) وموقع (Area / Shelf / Rack).
* **الاستعارة:** المستعير موظف أو طالب. مدة الإعارة وأقصى عدد كتب لكل دور يأتيان من `Faculty Library Setting`.
* **الغرامات والتلف:** مهمة يومية تحوّل الاستعارات المتأخرة إلى *Overdue* وتنشئ غرامة *Delay*. وتسجيل التلف ينشئ `Damage` وغرامة بسعر النسخة.
* **المعاملات بالعضوية:** مسار ثانٍ (`Library Transaction`) لإصدار النسخ وإرجاعها للأعضاء أصحاب `Library Membership` سارية.
* **طلبات التوريد** للمواد الجديدة.
* **API عام** لواجهة Vue (قائمة الكتب وتفاصيل الكتاب).

## دورة العمل بالترتيب

1. **الإعداد:** `Company` ثم `Faculty Library Setting` (مدة الإعارة، غرامة التأخير، أقصى عدد كتب لكل دور).
2. **الأماكن:** `Area` ثم `Shelf` ثم `Rack` (و`Library Section`).
3. **بيانات الفهرسة:** `Publisher` و`Author` و`Classification` و`Category`.
4. **المراجع:** `Book` و`Graduation Project` و`Magazine` وغيرها (الباركود يعرّف المرجع).
5. **النسخ:** `Item Copy` لكل نسخة (الحالة متاح، والسعر، والموقع).
6. **الأشخاص:** `Student` و`Employee` (و`Library Member` مع `Library Membership` لمسار العضوية).
7. **الاستعارة:** إنشاء `Item Borrowing` واعتماده ← يُحدَّد تاريخ الإرجاع ويُطبَّق حد الاستعارة وتصبح النسخة *Unavailable*.
8. **أثناء الاستعارة:** زر *Extend Borrowing* للتمديد، أو *Damage* (ينشئ `Damage` و`Fine`). ويوميًا تحوّل المهمة المجدولة المتأخر إلى *Overdue* وتنشئ غرامة *Delay*.
9. **الإرجاع:** زر *Returned* يعيد النسخة إلى *Available*.
10. **إخراج نسخة من التداول:** اعتماد `Unactivation Book` (تصبح النسخة *Damaged*، وإلغاؤه يعيدها *Available*).
11. **الكتالوج العام:** تعرض واجهة Vue الكتب عبر الـ API العام.

## الـ Doctypes (36)

| المجال | الـ Doctypes |
|---|---|
| المراجع | Book, Magazine, Research Paper, These And Dissertation, Graduation Project (+ Students, Supervisors), Audio Item, Video Item, E Item |
| الفهرسة | Author, Publisher, Category, Classification, Library Indexing |
| المكان الفعلي | Library Section, Area, Shelf, Rack |
| التداول | Item Copy, Item Borrowing, Library Transaction, Fine, Damage, Unactivation Book |
| الأشخاص | Student, Employee, Department, Library Member, Library Membership |
| الإعدادات والتوريد | Company, Faculty Library Setting, Supply Order (+ Items) |

## الـ API العام

يُستدعى بالشكل `http://<host>:<port>/api/method/<المسار>` بدون تسجيل دخول (`allow_guest`):

* `library_manegment.api.get_all_books.get_all_books`
* `library_manegment.api.get_book_details.get_book_details?book_name=<id>`

## المتطلبات

* [Frappe](https://frappeframework.com/) الإصدار 15 (عبر [bench](https://github.com/frappe/bench))
* Python 3.10 أو أحدث
* MariaDB (يختبر الـ CI على MariaDB 10.6)

لا حاجة لتطبيقات Frappe أخرى: كل Doctype يرتبط به التطبيق معرَّف داخله (تحققت منه بسكربت، ولا يأتي من Frappe إلا `User` و`Language`).

## التثبيت

```bash
bench get-app <repository-url> --branch <branch>
bench new-site <site-name>
bench --site <site-name> install-app library_manegment
bench start
```

الخطوات هي مسار Frappe القياسي ولم تُجرَّب كاملة على هذا الفرع. الواجهة الأمامية في مستودع منفصل `library_vue`.

## تاريخ الفروع

يجمع هذا الفرع فروع الفريق:

| المصدر | ما أضافه |
|---|---|
| `develop` | الأساس: نموذج البيانات وBook وItem Copy وLibrary Transaction والـ API العام |
| `esmail` | مسار الاستعارة: Item Borrowing وFine وDamage وسعر النسخة وحالاتها وغرامة التأخير والمهمة اليومية |
| `manar-branch` | `Department` و`Library Member` و`Library Membership` وعمل Unactivation Book |
| `main`، `nora` | موجودان أصلًا داخل `develop` |

عند اختلاف `develop` و`esmail` على الملف نفسه أُبقيت نسخة `esmail` لأنها الأحدث. تفاصيل الإصلاحات في رسائل الـ commits.

## الفريق

أصحاب الـ commits في تاريخ git: Manar Ahmed وIbtihal Homadi وZiad Mansor وEsmail Ebrahim Hamza وNora Hussain. مالكة منظمة GitHub: Shaima Riyadh.

TODO: أضف دور كل عضو وسياق المشروع (المقرر، الجامعة، السنة).

## الرخصة

MIT. راجع [license.txt](license.txt). TODO: املأ سطر حقوق النشر (`[year] [fullname]`) في `license.txt`.
