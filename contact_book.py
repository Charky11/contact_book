from utils.file_utils import load_contacts, save_contacts

DATA_FILE = "data/contacts.json"

def print_menu():
    print("\n📕 Меню справочника:")
    print("1. Показать все контакты")
    print("2. Добавить контакт")
    print("3. Найти контакт")
    print("4. Удалить контакт")
    print("5. Редактировать контакт")
    print("6. Выход")

def show_contacts(contacts):
    if not contacts:
        print("Контактов пока нет.")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")

def add_contact(contacts):
    name = input("Имя: ")
    phone = input("Телефон: ")
    email = input("Email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Контакт добавлен!")

def search_contact(contacts):
    query = input("Введите имя или номер: ").lower()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if results:
        show_contacts(results)
    else:
        print("Контакт не найден.")

def delete_contact(contacts):
    show_contacts(contacts)
    idx = int(input("Введите номер контакта для удаления: ")) - 1
    if 0 <= idx < len(contacts):
        removed = contacts.pop(idx)
        print(f"Контакт {removed['name']} удалён.")
    else:
        print("Некорректный номер.")


def edit_contact(contacts):
    name_to_edit = input("Введите имя контакта для редактирования: ").strip()
    found = False
    for contact in contacts:
        if contact['name'].lower() == name_to_edit.lower():
            print(f"Найден контакт: {contact}")
            new_name = input(f"Введите новое имя (оставьте пустым для '{contact['name']}'): ").strip()
            new_phone = input(f"Введите новый телефон (оставьте пустым для '{contact['phone']}'): ").strip()
            new_email = input(f"Введите новый email (оставьте пустым для '{contact['email']}'): ").strip()

            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email

            print(f"Контакт '{name_to_edit}' успешно обновлён: {contact}")
            found = True
            break
    if not found:
        print(f"Контакт '{name_to_edit}' не найден.")


def main():
    contacts = load_contacts(DATA_FILE)

    while True:
        print_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            show_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            edit_contact(contacts)
        elif choice == "6":
            save_contacts(DATA_FILE, contacts)
            print("До свидания!")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
  
