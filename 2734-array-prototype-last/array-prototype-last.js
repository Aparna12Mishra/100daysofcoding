Array.prototype.last = function() {
  return this.length ? this.slice(-1)[0] : -1;
};