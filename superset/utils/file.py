# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from werkzeug.utils import secure_filename
from slugify import slugify


def get_filename(model_name: str, model_id: int, skip_id: bool = False) -> str:
    model_name_fix = slugify(model_name)
    slug = secure_filename(model_name_fix)
    filename = slug if skip_id else f"{slug}_{model_id}"
    return filename if slug else str(model_id)
