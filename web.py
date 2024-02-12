import streamlit as st
import functions


todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



st.title("This app makes a List:")
st.subheader("You like lists")
st.write("Terry loves yogurt")

for todo in todos:
    st.checkbox(todo)

st.text_input("Enter a todo:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

#st.session_state

