from tkinter import *
import controller


def on_search():
    table.delete(0, END)
    name = search_entry.get()
    print("name " + name)
    users = controller.get_user_by_name(name)
    table.insert(END, *users)
    search_entry.delete(0, END)
    return


def on_manage():

    # Coleta de valor do ID do Usuário selecionado na tabela
    selected = table.get(table.curselection())
    split = selected.split("-")
    user = controller.get_user_by_id(split[0])

    # Coleta e visualização dos exames do usuário
    exams = controller.get_exams_by_user_id(user.id)
    create_exam_button.place(x="440", y="5")
    update_exam_button.place(x="530", y="5")
    delete_exam_button.place(x="620", y="5")
    exams_table.place(x="420", y="50")
    exams_table.insert(END, *exams)
    return


def on_create():

    # Criação da tela
    aux = Tk()
    aux.title("Adicionar Exame")
    aux.geometry("300x300")

    # Declaração das variáveis
    selected = table.get(table.curselection())
    user_id = selected.split("-")[0]
    doctors = controller.get_all_doctors()
    selected_doctor = StringVar(aux)
    selected_doctor.set(doctors[0])
    procedures = controller.get_all_procedures()
    selected_procedure = StringVar(aux)
    selected_procedure.set(procedures[0])
    is_multiple = IntVar()

    # Declaração dos componentes
    list_doctors = OptionMenu(aux, selected_doctor, *doctors)
    list_procedures = OptionMenu(aux, selected_procedure, *procedures)
    is_multiple_checkbox = Checkbutton(aux, text="Duas sessões?", variable=is_multiple, onvalue=1, offvalue=0)

    # Instanciação dos componentes na tela
    Label(aux, text="Selecione o médico:").pack()
    list_doctors.pack()
    Label(aux, text="Selecione o procedimento:").pack()
    list_procedures.pack()
    is_multiple_checkbox.pack()
    return


window = Tk()
window.geometry("800x420")
window.title("CRM")
search_entry = Entry(window, font=("Arial", 16))
table = Listbox(window, width=60, height=22, bg="#f7ffde")
search_button = Button(window, text="Search", command=on_search, font=("Arial", 14))
manage_button = Button(window, text="Manage", command=on_manage, font=("Arial", 14))
create_exam_button = Button(window, text="Create", command=on_create, font=("Arial", 14))
update_exam_button = Button(window, text="Update", command=on_manage, font=("Arial", 14))
delete_exam_button = Button(window, text="Delete", command=on_manage, font=("Arial", 14))
exams_table = Listbox(window, width=60, height=22, bg="#f7ffde")


def initial_screen():
    search_entry.place(x="5", y="10")
    table.place(x="5", y="50")
    search_button.place(x="250", y="5")
    manage_button.place(x="340", y="5")
    window.mainloop()
