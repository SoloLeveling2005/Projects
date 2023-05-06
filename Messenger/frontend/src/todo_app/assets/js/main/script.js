let comp = Vue.component('task', {
    props:{
        id: {
            type: Number,
            required: true
        },
        title: {
            type: String,
            required: true
        },
        description: {
            type: String,
            required: true
        },
        done: {
            type: String,
            required: true
        }
    },
    data: function () {
        return {}
    },
    methods:{
        delete_task: function (id) {
            my_vue.delete_task(Number(id))
        },
        perform_task: function (id) {
            my_vue.perform_task(Number(id))
        }
    },
    template: `
    <div class="task" :id="id" :key="id">
        <template v-if="done == 'in_progress'">
            <div class="title-description">
                <p class="title-text in_progress-title">{{title}}</p>
                <p class="description-text in_progress-description">{{description}}</p>
            </div>
            <div class="buttons">
                <button v-if="done == 'in_progress'" class="button-complate" @click="perform_task(id)">Complate</button>
                <button class="button-delete" @click="delete_task(id)">Delete</button>
            </div>
        </template> 
        <template v-else-if="done == 'ready'">
            <div class="title-description">
                <p class="title-text ready">{{title}}</p>
                <p class="description-text ready">{{description}}</p>
            </div>
            <div class="buttons">
                <button v-if="done == 'in_progress'" class="button-complate" @click="perform_task(id)">Complate</button>
                <button class="button-delete" @click="delete_task(id)">Delete</button>
            </div>
        </template>
    </div>
    `
})






let my_vue = new Vue ({
    el: '#tasks-section',
    data: function () {
        return {
            id_length: 0,
            tasks_data:[],
            delete_task_id:0,
        }
    },
    methods: {
        delete_task: function (task_id) {
            for (let index in this.tasks_data) {
                if (this.tasks_data[index].id == task_id) {
                    this.delete_task_id = index
                    document.querySelector(".message-for-user").style = "display:flex;"
                    break
                }
            }
        },
        perform_task: function (task_id) {
            for (let index in this.tasks_data) {
                if (this.tasks_data[index].id == Number(task_id)) {
                    this.tasks_data[index].done = "ready"
                }
            }
        }
    }
})


let create_task_button = new Vue ({
    el: '#create-task-block-button',
    data: function () {
        return {
        }
    },
    methods: {
        num_task: function (title,description) {
            if (document.querySelector(".input-name").value.trim() == "" || document.querySelector(".input-description").value.trim() == "") {
                  document.querySelector(".error").innerHTML = "Вы не заполнили все поля"
                  document.querySelector(".error").style = "display:flex;"
                  let error = () => {
                      document.querySelector(".error").innerHTML = ""
                      document.querySelector(".error").style = "display:none;"
                  }
                  setTimeout(error,2000)
            } else {
                    title = document.querySelector(".input-name").value.trim()
                    description = document.querySelector(".input-description").value.trim()
                    my_vue.tasks_data.push({
                        id:my_vue.id_length+=1,
                        title:title,
                        description:description,
                        done:"in_progress"
                    })
                    document.querySelector(".input-name").value = ""
                    document.querySelector(".input-description").value = ""
              }
        } 
    },
})
let confirm_delete_button = new Vue ({
    el: '#message-for-user',
    data: function () {
        return {
        }
    },
    methods: {
        confirm:function() {
            my_vue.tasks_data.splice(my_vue.delete_task_id, 1)
            document.querySelector(".message-for-user").style = "display:none;"
        },
        cancel:function() {
            my_vue.delete_task_id = 0
            document.querySelector(".message-for-user").style = "display:none;"
        }
    },
})
document.querySelector(".title-page").addEventListener('click', function() {
    document.querySelector("body").classList.toggle('dark');
    document.querySelector("body").classList.toggle('light');
});