<template>
  <form>
    <TextInput label="Progress" />
    <div class="grid md:grid-cols-2 md:gap-6">
      <TextInput label="AAC/S 150 mm2" />
      <TextInput label="456" />
    </div>
    <button type="submit"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
  </form>
</template>

<script>
import TextInput from './Forms/TextInput.vue';

export default {
  data() {
    return {
    }
  },
  components: {
    TextInput
  }
}
</script>