<template>
  <div class="home">
    <h1 class="title">Vuengo</h1>
    <hr />

    <div class="colums">
      <div class="column is-3 is-offset-3">
        <form v-on:submit.prevent="addTask">
          <h2 class="subtitle">Add Task</h2>
          <div class="field">
            <label for="" class="label">Description</label>
            <div class="control">
              <input type="text" class="input" v-model="description" />
            </div>
          </div>

          <div class="field">
            <label for="" class="label">Status</label>
            <div class="control">
              <div class="select">
                <select v-model="status">
                  <option value="todo">Todo</option>
                  <option value="done">Done</option>
                </select>
              </div>
            </div>
          </div>

          <div class="field">
            <div class="control">
              <button class="button is-link">Submit</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <div class="columns">
      <div class="column is-6">
        <h2 class="subtitle">Todo</h2>

        <div
          class="todo"
          v-for="task in tasks"
          v-if="task.status === 'todo'"
          v-bind:key="task.id"
        >
          <div class="card">
            <div class="card-content">{{ task.description }}</div>
            <footer class="card-footer">
              <a
                href=""
                class="card-footer-item"
                @click.prevent="setStatus(task.id, 'done')"
                >Done</a
              >
            </footer>
          </div>
        </div>
      </div>
      <div class="column is-6">
        <h2 class="subtitle">Done</h2>

        <div
          class="done"
          v-for="task in tasks"
          v-if="task.status === 'done'"
          v-bind:key="task.id"
        >
          <div class="card">
            <div class="card-content">{{ task.description }}</div>
            <footer class="card-footer">
              <a
                href=""
                class="card-footer-item"
                @click.prevent="deleteTask(task.id)"
                >Delete</a
              >
            </footer>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Home",
  data() {
    return {
      tasks: [],
      description: "",
      status: "todo",
    };
  },
  mounted() {
    this.getTasks();
  },
  methods: {
    getTasks() {
      axios({
        method: "get",
        url: "http://127.0.0.1:8000/tasks/",
        auth: {
          username: "admin",
          password: "123123",
        },
      }).then((res) => {
        this.tasks = res.data;
      });
    },
    addTask() {
      if (this.description) {
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/tasks/",
          data: {
            description: this.description,
            status: this.status,
          },
          auth: {
            username: "admin",
            password: "123123",
          },
        })
          .then((res) => {
            let newTask = {
              id: res.data.id,
              description: res.data.description,
              status: res.data.status,
            };

            this.tasks.push(newTask);
            this.description = "";
            this.status = "todo";
          })
          .catch((e) => {
            console.log("error", e);
          });
      }
    },
    setStatus(task_id, status) {
      const task = this.tasks.filter((task) => task.id === task_id)[0];
      let description = task.description;
      axios({
        method: "put",
        url: "http://127.0.0.1:8000/tasks/" + task_id + "/",
        headers: {
          "Content-Type": "application/json",
        },
        data: {
          status: status,
          description: description,
        },
        auth: {
          username: "admin",
          password: "123123",
        },
      }).then(() => {
        task.status = status;
      });
    },
    deleteTask(task_id) {
      axios({
        method: "delete",
        url: "http://127.0.0.1:8000/tasks/" + task_id + "/",
        headers: {
          "Content-Type": "application/json",
        },
        auth: {
          username: "admin",
          password: "123123",
        },
      })
        .then((res) => {
		  this.tasks = this.tasks.filter(task => task.id !== task_id)
        })
        .catch((e) => {
          console.log("error", e);
        });
    },
  },
};
</script>

<style lang="scss">
.select,
select {
  width: 100%;
}
.card {
  margin-bottom: 20px;
}
.done {
  opacity: 0.3;
}
</style>
