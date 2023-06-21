<script setup>
function mergeArrays(A, B) {
  const merged = [];
  let i = 0;
  let j = 0;

  // 遍历数组 A 和 B
  while (i < A.length && j < B.length) {
    if (A[i] < B[j]) {
      merged.push(A[i]);
      i++;
    } else {
      merged.push(B[j]);
      j++;
    }
  }

  // 将剩余的元素添加到 merged 数组中
  while (i < A.length) {
    merged.push(A[i]);
    i++;
  }

  while (j < B.length) {
    merged.push(B[j]);
    j++;
  }

  return merged;
}

// 示例用法
const A = [1, 3, 5, 7];
const B = [2, 4, 6, 8];

const C = mergeArrays(A, B);
console.log(C); // [1, 2, 3, 4, 5, 6, 7, 8]



import { ref,defineProps } from 'vue';

const props = defineProps({
  auths: Array
})
const prize = ref([
  {
    value: '一级奖品',
    active: false
  },
  {
    value: '二级奖品',
    active: false
  },
  {
    value: '三级奖品',
    active: false
  },
  {
    value: '四级奖品',
    active: false
  },
  {
    value: '五级奖品',
    active: false
  },
  {
    value: '六级奖品',
    active: false
  },
  {
    value: '七级奖品',
    active: false
  },
  {
    value: '八级奖品',
    active: false
  },
])
const count = ref(10)
const handleLottery = () => {
  if(props.auths.length === 0) {
    console.log('请邀请客户');
    return
  }
  let index = 0
  const timer = setInterval(() => {
    count.value = count.value - 1

    if(count === 0) {
      clearInterval(timer)
    }

    index ++
    if (index >= prize.value.length) {
      index = 0
    }
    prize.value = prize.value.map(item => {
      item.active = false
      return item
    })
    prize.value[index].active = true;
  }, count.value * 100);


  const randomIndex = Math.floor(Math.random() * prize.value.length);

  prize.value[randomIndex].active = true;
}
</script>
<template>
  <div>
    <div class="price">
      <div v-for="(item, key) in prize" :key="key" >
        <span :class="item.active? 'active': 'no-active'" >
          {{ item.value }}
        </span>
      </div>
      <el-button @click="handleLottery" >抽奖</el-button>
    </div>
  </div> 
</template>