import streamlit as st

st.title("📝 To-Do List")

# Input task
task = st.text_input("Enter your task:")

# Add task
if st.button("Add Task"):
    if task.strip() == "":
        st.warning("Please enter a task.")
    else:
        if "tasks" not in st.session_state:
            st.session_state.tasks = []
        st.session_state.tasks.append(task)
        st.success("Task added!")

# Display tasks
st.subheader("Your Tasks")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

for i, task in enumerate(st.session_state.tasks):
    st.write(f"{i + 1}. {task}")

# Clear all tasks
if st.button("Clear All"):
    st.session_state.tasks = []
    st.success("All tasks cleared!")
