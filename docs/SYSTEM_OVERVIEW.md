# System overview

Details moved out of the README. Read from the code of the `integration` branch; not run on a live Frappe site.

## Typical workflow

1. **Set up** the faculty: `Company`, then `Faculty Library Setting` (loan period, delay fine, maximum books per role).
2. **Define places:** `Area` -> `Shelf` -> `Rack` (and `Library Section`).
3. **Define catalogue data:** `Publisher`, `Author`, `Classification`, `Category`.
4. **Add reference items:** `Book`, `Graduation Project`, `Magazine`, ... (the barcode identifies the item).
5. **Create copies:** one `Item Copy` per physical copy (status *Available*, price, location).
6. **Register people:** `Student` and `Employee` (and `Library Member` + `Library Membership` for the membership flow).
7. **Borrow:** create and submit an `Item Borrowing` -> due date is set, loan limit is enforced, the copy becomes *Unavailable*.
8. **During the loan:** *Extend Borrowing*, or *Damage* (creates `Damage` + `Fine`). Every day the scheduler turns late loans into *Overdue* and creates a *Delay* `Fine`.
9. **Return:** the *Returned* button sets the copy back to *Available*.
10. **Retire a copy:** submit an `Unactivation Book` (copy becomes *Damaged*; cancelling restores *Available*).
11. **Public catalogue:** the Vue app lists books via the public API.

## Doctypes (36)

| Area | Doctypes |
|---|---|
| Reference items | Book, Magazine, Research Paper, These And Dissertation, Graduation Project (+ Students, Supervisors), Audio Item, Video Item, E Item |
| Cataloguing | Author, Publisher, Category, Classification, Library Indexing |
| Physical location | Library Section, Area, Shelf, Rack |
| Circulation | Item Copy, Item Borrowing, Library Transaction, Fine, Damage, Unactivation Book |
| People | Student, Employee, Department, Library Member, Library Membership |
| Settings and supply | Company, Faculty Library Setting, Supply Order (+ Items) |

## Public API

Called as `http://<host>:<port>/api/method/<path>`, no login required (`allow_guest`):

* `library_manegment.api.get_all_books.get_all_books`
* `library_manegment.api.get_book_details.get_book_details?book_name=<id>`

## Setup

```bash
bench get-app <repository-url> --branch <branch>
bench new-site <site-name>
bench --site <site-name> install-app library_manegment
bench start
```

The setup steps follow the standard Frappe flow and have not been run end to end on this branch. The front end lives in the separate `library_vue` repository.
