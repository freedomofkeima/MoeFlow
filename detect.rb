require "pp"
require "rmagick"
# Put nagadomi/animeface-2009 path here
require "/home/ec2-user/animeface-2009/animeface-ruby/AnimeFace"

if ARGV.size == 0
  warn "Usage: #{$0} <source-file> <target-dir>"
  exit(-1)
end

image = Magick::ImageList.new(ARGV[0])
faces = AnimeFace::detect(image)
counter = 0
pp faces
faces.each do |ctx|
  next if ctx["likelihood"] < 0.7
  counter = counter + 1
  filename = File.basename(ARGV[0]).split(".").first + "_out_" + counter.to_s + ".jpg"
  output = File.join(ARGV[1], filename)
  face = ctx["face"]
  x = [face["x"] - 30, 0].max
  y = [face["y"] - 30, 0].max
  width = [face["width"] + 60, image.columns - x].min
  height = [face["height"] + 60, image.rows - y].min
  gc = image.crop(x, y, width, height)
  gc.write(output)
end

