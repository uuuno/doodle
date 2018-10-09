<template>
    <div>
        <p>Hello, World!</p>
	<counter/>
	<avatar username="Jane Doe"></avatar>
	<lunar-calendar
    @change="onChange"
    :firstDayOfWeek="parseInt(firstDayOfWeek)"
    :disableDaysBeforeToday="disableDaysBeforeToday"
    :defaultDate="defaultDate"
    :showLunarButton="showLunarButton"
  ></lunar-calendar>
    </div>
</template>

<script>

import Counter from "./Counter"
import Avatar from "vue-avatar"
import lunarCalendar from 'vue-lunar-calendar'

export default{
       components: {Counter, Avatar, lunarCalendar},
}


</script>

<style>
p{
	font-size: 20px;
}
</style>