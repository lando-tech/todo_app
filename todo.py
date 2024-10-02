from db import MyDB

db_conn = MyDB()
rows = db_conn.query_db()

def main_loop():
    should_continue = True
    selections = [1, 2, 3, 4]

    while should_continue:
        add_task = int(input("Select from the following options:"
                     "\n\t[1] Add task"
                     "\n\t[2] View tasks"
                     "\n\t[3] Delete task"
                     "\n\t[4] Exit\n"))

        if add_task not in selections:
            print("Please select from options 1-4.")
            main_loop()

        if add_task == 4:
            db_conn.close_db()
            should_continue = False
            break
        elif add_task == 1:
            task = input("\nPlease enter a task: ")
            db_conn.add_entry(task, "Incomplete")
        elif add_task == 2:
            for row in rows:
                print(f"\t{row}\n")
        elif add_task == 3:
            print("\nEnter the task ID# to delete: ")
            for i in rows:
                print(i)
            to_delete = int(input(""))
            for row in rows:
                if row[0] == to_delete:
                    db_conn.delete_entry(row[0])
                else:
                    print("Entry selected does not exist.")
                    continue
