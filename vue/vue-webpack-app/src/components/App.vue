<template>
    <div>
        <p>Hello, World!</p>
	<counter/>
	<avatar username="Jane Doe"></avatar>
    </div>
</template>

<script>
import Counter from './Counter'
import Avatar from 'vue-avatar'

 export default {
     components: {Counter, Avatar},
}
</script>