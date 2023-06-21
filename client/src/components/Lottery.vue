<script setup>
import { ref ,defineProps } from 'vue';
const emit = defineEmits(['inviteFriends']);
defineProps({
  auths: Array
})
const friends = ref([null, null, null, null])
const handleInviteFriends = () => {
  emit('inviteFriends')
}
</script>
<template>
  <div class="lottery">
    <h1>
      一重礼 助力拆包！好友注册并开启红包
    </h1>
    <p>
      以下是文案
    </p>
    <div class="content flex justify-between">
      <el-button @click="handleInviteFriends">邀请好友</el-button>
      <el-button>下载发车</el-button>
    </div>
    <div class="auth">用户头像</div>
    <div class="friends flex justify-between" v-if="auths.length === 0" >
      <span @click="handleInviteFriends" class="pd-10" v-for="item, key in friends" :key="key" >+</span>
    </div>
    <div class="friends flex justify-between" v-if="auths.length > 0" >
      <span class="pd-10" v-for="item, key in auths" :key="key" >{{ item }}</span>
    </div>
  </div> 
</template>