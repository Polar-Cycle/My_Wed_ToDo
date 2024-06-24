import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    my_todo = st.session_state["new_todo"] + "\n"
    todos.append((my_todo))
    functions.write_todos(todos)


st.title("My ToDo App")
st.subheader("Another day in paradise.")
st.write("This app increases your productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo[0:20])
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo[0:20]]
        st.rerun()

# the "" before can be replaced with label=some text and will
# create a small label above the box
st.text_input(label="add todo", label_visibility='hidden', placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
