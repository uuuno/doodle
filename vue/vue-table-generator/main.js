'use strict';

var vTable = Vue.extend({
  data: function(){
    return {
        table: [
          [1,1,1],
          [1,1,1],
          [1,1,1]
        ]
    }
  },
  template: `
  <div>
    <button v-on:click="add_row()">Row+</button>
    <button v-on:click="add_col()">Col+</button>
    {{ num_rows }}, {{ num_cols }}
    <table>
      <tr v-for="row in table">
        <td v-for="col in row">{{col}}</td>
      </tr>
    </table>
  </div>
  `,
  methods: {
    add_row: function(){
      var new_row = [];
      for (var i = 0; i < this.num_cols; i++) {
        new_row.push(1);
      }
      this.table.push(new_row);
    },
    add_col: function(){
      for (var i = 0; i < this.num_rows; i++) {
        this.table[i].push(1);
      }
    }
  },
  computed: {
    num_rows: function(){
      return (this.table).length
    },
    num_cols: function(){
      return (this.table[0]).length
    }
  }
});


var components = new Vue({
  el: '#app',
  data:{
    totalCount: 0
  },
  methods:{
    increTotal: function(){
      this.totalCount++;
    }
  },
  components: {
    'v-table-generator': vTable
  }
});
