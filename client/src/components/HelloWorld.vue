<script setup>
import { ref } from 'vue'

defineProps({
  msg: String,
})

const count = ref(0)
</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="card">
    <button type="button" @click="count++" class="bg-red-500">count is {{ count }}</button>
    <li v-for="task in tasks" :key="task.id">
        <h2>{{ task.bagian }}</h2>
    </li>
  </div>

  <p>
    Check out
    <a href="https://vuejs.org/guide/quick-start.html#local" target="_blank">create-vue</a>, the official Vue + Vite
    starter
  </p>
  <p>
    Install
    <a href="https://github.com/vuejs/language-tools" target="_blank">Volar</a>
    in your IDE for a better DX
  </p>
  <p class="read-the-docs">Click on the Vite and Vue logos to learn more</p>
</template>

<script>
import axios from 'redaxios'

export default {
  data() {
    return {
      // tasks
      books: [],
      tasks: ['']
    }
  },
  methods: {
    async getData() {
      try {
        // fetch tasks
        const response = await this.$http.get('http://127.0.0.1:8000/api/pengadaan/');
        // set the data returned as tasks
        this.tasks = response.data;
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
    getBooks() {
      const path = 'http://127.0.0.1:8000/api/pengadaan/';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // estlint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    // Fetch tasks on page load
    // this.getData();
    this.getBooks();
  }
}
</script>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
