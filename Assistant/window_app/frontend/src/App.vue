<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <section class="chat">
    <div class="message message--user-1">
      <time class="message__time">21.02.2017 21:12:07</time>
      <div class="message__text">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis at purus nibh. Cras metus nulla, vestibulum in auctor ac, fermentum vitae tellus.</p>
      </div>
    </div>
    <div class="message message--user-2">
      <time class="message__time">21.02.2017 21:12:07</time>
      <div class="message__text">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis at purus nibh. Cras metus nulla, vestibulum in auctor ac, fermentum vitae tellus.</p>
      </div>
    </div>
    <div class="message message--user-2">
      <time class="message__time">21.02.2017 21:12:07</time>
      <div class="message__text">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis at purus nibh. Cras metus nulla, vestibulum in auctor ac, fermentum vitae tellus.</p>
      </div>
    </div>
    <div class="message message--user-1">
      <time class="message__time">21.02.2017 21:12:07</time>
      <div class="message__text">
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis at purus nibh. Cras metus nulla, vestibulum in auctor ac, fermentum vitae tellus.</p>
      </div>
    </div>

    <div style="position: fixed; bottom: 0; left: 0; width: 100%; display: flex; align-items: center;  background-color: #181818;">
<!--      <input type="text" style="padding: 10px; font-size: 18px; margin: 15px; outline:none; width: calc(100% - 170px);" autocomplete="off">-->
<!--      <button style="font-size: 18px; padding: 10px; cursor: pointer">Отправить</button>-->
      <input type="text" style="padding: 10px; font-size: 18px; margin: 15px; outline:none; width: calc(100% - 40px);" autocomplete="off">
    </div>
  </section>
</template>

<style scoped>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  .chat {
    background-color: #424242;
    padding: 10px;
    width: 100vw;
    height: 100vh;
  }

  .message {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    align-items: center;

  }
  .message--user-1 + .message--user-2,
  .message--user-2 + .message--user-1 {
    margin-top: 1em;
  }
  .message--user-1 + .message--user-1,
  .message--user-2 + .message--user-2 {
    margin-top: .5em;
  }
  .message__time {
    font-size: 10px;
    color: #ccc;
    width: 100%;
    margin: 0 0 5px 5px;
  }
  .message__author-pic {
    margin: 0 10px 0 0;
  }

  .message__text {
    padding: 10px;
    border-radius: 10px;
    border: 0;
    background-color: #1A1A1A;
    max-width: 70%;
    color: rgba(255, 255, 255, 0.88);
  }

  .message--user-2 {
    justify-content: flex-end;
  }
  .message--user-2 .message__time {
    text-align: right;
    margin: 0 5px 5px 0;
  }
  .message--user-2 .message__author-pic {
    order: 1;
    margin: 0 0 0 10px;
  }
  .message--user-2 .message__text {
    color: rgba(255, 255, 255, 0.88);
  }
</style>
