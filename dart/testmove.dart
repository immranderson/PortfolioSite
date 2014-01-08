import 'dart:html';
import 'dart:svg';

RectElement rect;
int pos = 0;
int dest = 300;

void main() {
  
  rect = querySelector("#rect");
  document.animationFrame.then(animate);
  
}

animate(num delta) {
  
  if (pos < dest) {
    pos += 2;
    rect.attributes['y'] = pos.toString();
    document.animationFrame.then(animate);
  }
  
}
