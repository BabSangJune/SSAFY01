<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation" @keyup.enter="signup">
    </div>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'Signup',
  data: function () {
    return {
      // 입력 양방향 데이터
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      },
    }
  },
  methods: {
    signup: function () {
      console.log(this.credentials)
      
    }
  }
}
</script>
