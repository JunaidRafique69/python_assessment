<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <button @click="createTask" class="bg-black hover:bg-gray-800 text-white font-bold py-2.5 px-5 rounded">
        Create Task
    </button>
</template>

<script>
import axios from 'axios';

export default {
    emits: ['task-created'],
    methods: {
        async createTask() {
            const response = await axios.post('http://localhost:8000/task/');
            this.$emit('task-created', response.data);
        }
    }
}
</script>