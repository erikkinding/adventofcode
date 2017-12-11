import java.util.*;

HashMap<String, PVector> moves = new HashMap<String, PVector>();

void setup()
{
  size(640, 480, P3D);
  
  String[] inp = loadStrings("../../input/eleven.txt")[0].split(",");
  
  moves.put("n", new PVector(0, 1, -1));
  moves.put("ne", new PVector(1, 0, -1));
  moves.put("se", new PVector(1, -1, 0));
  moves.put("s", new PVector(0, -1, 1));
  moves.put("sw", new PVector(-1, 0, 1));
  moves.put("nw", new PVector(-1, 1, 0));
  
  
}



void draw()
{
  rect(10, 10, 10, 10);
}