import { createApp } from 'vue'
import App from '~/App.vue';
import { Page, ActionBar, GridLayout, Button, Img, Label } from 'nativescript-vue-web';

Vue.component('Page', Page);
Vue.component('ActionBar', ActionBar);
Vue.component('GridLayout', GridLayout);
Vue.component('Button', Button);
Vue.component('Img', Img);
Vue.component('Label', Label);

createApp(App).mount('#app')
