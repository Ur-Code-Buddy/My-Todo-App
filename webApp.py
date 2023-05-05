import streamlit as st
import functions

 hide_st_style = """
        <style>
        #MainMenu{visibility:hidden;}
        footer{visibility: hidden;}
        </style>
        """

        st.markdown(hide_st_style,unsafe_allow_html=True)

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is My todo App")
st.write("This app aims to increase productivity - Bai")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key = todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._rerun()

st.text_input(label = "", placeholder="Add new todo: ", on_change=add_todo, key='new_todo')


#st.session_state
