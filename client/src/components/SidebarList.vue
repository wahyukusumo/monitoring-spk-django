<template>
  <li>
      <a href="#"
        class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group">
        <slot></slot>
        <span class="ml-3">{{ this.name }}</span>
      </a>
  </li>
</template>

<script>
export default {
  data() {
    return {
    };
  },
  methods: {
  },
  props:['name', 'toRouter']
};
</script>