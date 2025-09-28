<script lang="ts">
    import {Button} from "$lib/components/ui/button"

    let count = $state(0)

    let inc = () => {
        count++
    }
</script>


<div>Count: <span>{count}</span></div>
<Button onclick={inc}>Inc</Button>