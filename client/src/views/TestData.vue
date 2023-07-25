<template>
  <h2 class="text-white">{{ tasks }}</h2>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      // tasks
      tasks: ['']
    }
  },
  methods: {
    async getData() {
      try {
        // fetch tasks
        const response = await axios.get(
          "http://127.0.0.1:8000/api/pengadaan/"
        );
        // set the data returned as tasks
        this.tasks = response.data;
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
  },
  created() {
    // Fetch tasks on page load
    this.getData();
  }
}
</script>