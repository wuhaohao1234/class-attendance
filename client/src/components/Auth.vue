
<script setup>
import { defineProps } from 'vue';
defineProps({
  phone: String
})

</script>
<template>
    <div class="auth">
      <input type="text" :placeholder="'欢迎您' + phone" >
      <el-button>奖励记录</el-button>
      <el-button>规则</el-button>
    </div>
</template>

<style>

</style>