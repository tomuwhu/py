class ML {
    #begin
    push( k ) {
        this.#begin = { key: k, next: this.#begin }
    }
    pop() {
        let pv = null
        if ( pv = this.#begin) {
            this.#begin = this.#begin.next
            return pv.key
        }
    }
}
const ml = new ML
ml.push(1); ml.push(2); ml.push(3)

console.log(ml.pop())
console.log(ml.pop())
console.log(ml.pop())
