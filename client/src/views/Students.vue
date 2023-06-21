<script setup>


import { ref } from 'vue';
import Auth from '../components/Auth.vue'
import lottery from '../components/lottery.vue';
import lotteryFunction from '../components/LotteryFunction.vue';
const phone = ref('18329723317')
const auths = ref([])
const inviteFriends = () => {
  auths.value = [...auths.value, 'auth']
}
</script>
<template>
  <div class="banner"  >
    <Auth :phone="phone" />
    <lottery @inviteFriends="inviteFriends" :auths="auths"/>
    <lotteryFunction :auths="auths" />
  </div>
</template>

<style>

</style>