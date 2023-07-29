<template>
  <button @click="this.modalShow = true" class="mx-2 font-medium text-blue-600 dark:text-blue-500 hover:underline">{{ buttonText }}</button>

  <!-- Main modal -->
  <div id="defaultModal" tabindex="-1" aria-hidden="true" v-if="this.modalShow"
    class="fixed top-0 left-0 right-0 z-50 w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
    <div class="relative mx-auto w-full max-w-2xl max-h-full">
      <!-- Modal content -->
      <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
        <!-- Modal header -->
        <div class="flex items-start justify-between p-4 border-b rounded-t dark:border-gray-600">
          <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
            {{ this.modalTitle }}
          </h3>
          <button type="button" @click="this.modalShow = false"
            class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
            data-modal-hide="defaultModal">
            <i class="fa-solid fa-close"></i>
            <span class="sr-only">Close modal</span>
          </button>
        </div>
        <!-- Modal body -->
        <div class="p-6 space-y-6">
          <slot name="body"></slot>
        </div>
        <!-- Modal footer -->
        <div class="flex items-center p-6 space-x-2 border-t border-gray-200 rounded-b dark:border-gray-600">
          </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      modalShow: false
    }
  },
  props: ['modalTitle', 'buttonText']
}
</script>