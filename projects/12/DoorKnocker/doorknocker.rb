require 'rdf'
require 'sparql'
require 'rest-client'
require 'json'
require 'time'
require 'sinatra'
require 'haml'
require 'sinatra/partial'
require 'erb'
require "uuidtools"

#set :public_folder, '/front-end/public'

get '/' do
     haml :index, :format => :html5
end

post '/knockknock' do
    knockknock()
    haml :results, :format => :html5
end

def knockknock
  json = JSON.parse(request.body.read)
  $stderr.puts "I got some JSON: #{json.inspect}"
  query = json['query']
  requester = json['requester']
  File.open('/tmp/query', 'w') {|f| f.write(query)}
  @result = File.read('/tmp/query')
  $stderr.puts "I got some query: #{@result}"

end

            