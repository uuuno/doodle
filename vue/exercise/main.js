'use strict';

var helloVue = new Vue({
  el: '.helloVue',
  data: {
    name: 'uuuno'
  }
});

var toDo = new Vue({
  el: '.toDo',
  data: {
    newTodo: '',
    message: '',
    todos: [
      {
        title: 'buy egg',
        isDone: false
      },
      {
        title: 'stydy Vue.js',
        isDone: false
      },
      {
        title: 'go fishing',
        isDone: true
      }
    ]
  },
  methods:{
    addToDo: function(){
      this.message = "";
      if(this.newTodo != ''){
        var value = {
          title: this.newTodo,
          isDone: false
        }
        this.todos.push(value);
        this.newTodo = '';
      }else{
        this.message = "ToDo is Empty!";
      }
    },
    deleteToDo: function(index){
      this.todos.splice(index, 1);
    }
  }
});

// var checkName = new Vue({
//   el: '.checkName',
//   data: {
//     myName: 'sas'
//   }
// });

var checkName = new Vue({
  el: '.checkName',
  data: {
    myName: ''
  }
});

var computed = new Vue({
  el: '.computed',
  data: {
    height: '',
    weight: ''
  },
  computed: {
    bmi: function(){
      return (this.weight)/(((this.height)*0.01)**2);
    }
  }
});
