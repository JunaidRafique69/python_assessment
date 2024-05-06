<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-gradient-to-t from-white to-slate-300">
    <TaskButton @task-created="handleTask" />
    <div v-if="tasks.length > 0" class="mt-5 bg-gray-200 rounded-xl p-4 w-[20%]">
      <h1 class="text-2xl font-bold px-4">Tasks</h1>
      <ul class="px-5 mx-4">
        <li v-for="task in tasks" :key="task.task_id" class="px-4 py-4 sm:px-6 list-disc">
          <span>Task Id : {{ task.task_id }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import TaskButton from './components/TaskButton.vue';

export default {
  components: { TaskButton },
  data() {
    return {
      tasks: []
    };
  },
  methods: {
    handleTask(task) {

      this.tasks.push({ ...task });
    }
  }
}
</script>
