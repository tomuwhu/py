async function f() {
    await new Promise(resolve => setTimeout(resolve, 1000))
}