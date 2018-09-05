'use strict';

var vTable = Vue.extend({
  data: function(){
    return {
        table: [
          ['a','b','c'],
          [1,1,1],
          [1,1,1]
        ],
        visible: false
    }
  },
  template: `
  <div>
    <button v-on:click="add_row()">Row+</button>
    <button v-on:click="add_col()">Col+</button>
    <br><br>Rows: {{ num_rows }}<br>
    Cols: {{ num_cols }}
    <table>
      <tr v-for="(row, row_index) in table">
        <td v-for="(col, col_index) in row">
          <input v-model="table[row_index][col_index]" v-on:keyup.enter="visible=false" v-on:blur="visible=false" ref="r1"/>
        </td>
      </tr>
    </table>

    <div class="res_md">
      <div v-for="(row, row_index) in table">
        <div v-if="row_index==0">
          | <span v-for="col in row"> {{col}} |</span><br>
          | <span v-for="col in row"> ---- |</span>
        </div>
        <div v-else>
          | <span v-for="col in row"> {{col}} |</span>
        </div>
      </div>
    </div>

    <div class="res_html">
      <div>&lt;table&gt;</div>
      <div v-for="(row, row_index) in table">
        <div v-if="row_index==0">
        &lt;tr&gt;<span v-for="col in row">&lt;th&gt; {{col}} &lt;/th&gt;</span>&lt;/tr&gt;
        </div>
        <div v-else>
        &lt;tr&gt;<span v-for="col in row">&lt;td&gt; {{col}} &lt;/td&gt;</span>&lt;/tr&gt;
        </div>
      </div>
      <div>&lt;/table&gt;</div>  
    </div>

  </div>
  `,
  methods: {
    add_row: function(){
      var new_row = [];
      for (var i = 0; i < this.num_cols; i++) {
        new_row.push('X');
      }
      this.table.push(new_row);
    },
    add_col: function(){
      for (var i = 0; i < this.num_rows; i++) {
        this.table[i].push('X');
      }
    },
    ch_text: function() {
      this.visible = true
      this.$nextTick(function () { this.$refs.r1.focus() })
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
